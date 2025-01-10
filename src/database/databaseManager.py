import sqlite3
from typing import List, Tuple
from database.populate import *
from database.sql_queries import SQL_QUERIES
import sqlite3
import os
import globals  # Présumé défini pour gérer le rôle de l'utilisateur


class SQLiteManager:
    def __init__(
        self,
        db_path: str = "plm_database.db",
        schema_path: str = "src/database/schema.sql",
    ):
        """
        Initialise la connexion SQLite.
        - Vérifie les permissions utilisateur (`admin` ou `viewer`).
        - Initialise et peuple la base de données si elle n'existe pas.
        """
        self.db_path = db_path
        self.schema_path = schema_path
        self.connection = None

        # Vérifie le rôle de l'utilisateur
        self.is_admin = globals.current_user == "admin"
        # Initialise la base de données si nécessaire
        if not os.path.exists(self.db_path):
            print(
                f"La base de données '{self.db_path}' n'existe pas. Initialisation..."
            )
            self.connect()
            self._initialize_database()
            self._peuplage_database()
        else:
            self.connect()

    def connect(self):
        """Établit une connexion à la base de données SQLite."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"Connecté à la base de données: {self.db_path}")
        except sqlite3.Error as e:
            print(f"Erreur lors de la connexion: {e}")

    def close(self):
        """Ferme la connexion SQLite."""
        if self.connection:
            self.connection.close()
            print("Connexion fermée.")

    def _initialize_database(self):
        """Initialise la base de données en exécutant le script SQL de schéma."""
        if not self.connection:
            raise ConnectionError(
                "Connexion non établie lors de l'initialisation de la base de données."
            )

        if os.path.exists(self.schema_path):
            try:
                with open(self.schema_path, "r", encoding="utf-8") as file:
                    sql_script = file.read()
                cursor = self.connection.cursor()
                cursor.executescript(sql_script)
                self.connection.commit()
                print(
                    f"Base de données initialisée avec succès à partir de '{self.schema_path}'."
                )
            except Exception as e:
                print(f"Erreur lors de l'initialisation de la base de données: {e}")
        else:
            print(f"Le fichier de schéma '{self.schema_path}' est introuvable.")

    def is_table_empty(self, table_name: str) -> bool:
        """
        Vérifie si une table est vide.
        :param table_name: Nom de la table à vérifier.
        :return: True si la table est vide, False sinon.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            return count == 0
        except sqlite3.Error as e:
            print(f"Erreur lors de la vérification de la table {table_name}: {e}")
            return False

    def execute_query(self, query, params=None):
        """
        Exécute une requête SQL et retourne les résultats s'ils existent.
        """
        cursor = self.connection.cursor()
        try:
            # Exécution de la requête avec ou sans paramètres
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # Récupérer les résultats s'ils existent
            result = cursor.fetchall() if cursor.description else True

            # Commit si ce n'est pas une requête de lecture
            self.connection.commit()

            return result
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            return False
        finally:
            cursor.close()

    def get_query_executor(self):
        """
        Retourne la méthode execute_query pour usage externe.
        """
        return self.execute_query

    def _peuplage_database(self):
        if not self.connection:
            raise ConnectionError(
                "Connexion non établie lors de l'initialisation de la base de données."
            )
        else:

            query_executor = self.get_query_executor()
            # Vérifiez chaque table et exécutez son peuplement si elle est vide
            if self.is_table_empty("Product_info"):
                populate_products(query_executor)
            if self.is_table_empty("Details_Couts"):
                populate_costs(query_executor)
            if self.is_table_empty("Ingredients"):
                populate_ingredients(query_executor)
            if self.is_table_empty("Composition_produit"):
                populate_compositions(query_executor)
            if self.is_table_empty("Fournisseurs_Distributeurs"):
                populate_fournisseurs_distributeurs(query_executor)
            if self.is_table_empty("Marchandises"):
                populate_marchandises(query_executor)
            if self.is_table_empty("Usines_Entrepots"):
                populate_usines_entrepots(query_executor)
            if self.is_table_empty("Process"):
                populate_process(query_executor)
            if self.is_table_empty("Lots"):
                populate_lots(query_executor)
            if self.is_table_empty("Stock"):
                populate_stock(query_executor)
            if self.is_table_empty("Historique_Process"):
                populate_historique_process(query_executor)
            if self.is_table_empty("Distributions"):
                populate_distributions(query_executor)
            print("Peuplement terminé")

    def fetch_query(self, table_name: str):
        """
        Exécute une requête SQL définie dans SQL_QUERIES en fonction du nom de la table.

        :param table_name: Le nom de la table ou clé utilisée pour récupérer la requête dans SQL_QUERIES.
        :return: Les résultats de la requête ou None en cas d'erreur.
        """
        if table_name not in SQL_QUERIES:
            print(f"Erreur : la table '{table_name}' n'existe pas dans SQL_QUERIES.")
            return None

        query = SQL_QUERIES[table_name]

        try:
            result = self.execute_query(query)
            return result
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête pour '{table_name}': {e}")
            return None
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
            return None

    def update_row(self, table_name, data_line):
        """
        Met à jour une ligne dans une table donnée.

        :param table_name: Nom de la table.
        :param data_line: Dictionnaire contenant les colonnes et leurs nouvelles valeurs,
                        y compris 'id' pour spécifier la ligne à mettre à jour.
        """

        if "id" not in data_line.keys():
            raise ValueError(
                "La clé 'id' est requise dans 'data_line' pour identifier la ligne à mettre à jour."
            )

        # Préparer la clause SET et les paramètres
        set_clause = ", ".join(
            [f"{key} = ?" for key in data_line.keys() if key != "id"]
        )
        query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        params = tuple(data_line[key] for key in data_line.keys() if key != "id") + (
            data_line["id"],
        )

        # Exécuter la requête
        if self.execute_query(query, params):
            print(f"Ligne avec id {data_line['id']} mise à jour dans '{table_name}'.")

    def delete_row(self, table_name, row_id):
        """
        Supprime une ligne dans une table donnée.
        """
        query = f"DELETE FROM {table_name} WHERE id = ?"
        if self.execute_query(query, (row_id,)):
            print(f"Ligne avec id {row_id} supprimée de '{table_name}'.")

    def get_row_suggestion(self, table_name):
        """
        Récupère les suggestions basées sur les relations de clés étrangères.
        """
        foreign_key_query = f"""
        PRAGMA foreign_key_list({table_name});
        """
        foreign_keys = self.execute_query(foreign_key_query)

        suggestions = {}
        if foreign_keys is not None:
            for fk in foreign_keys:
                fk_table = fk[2]  # Table référencée
                fk_column = fk[3]  # Colonne locale (id de la clé étrangère)
                ref_column = fk[4]  # Colonne dans la table référencée

                # Vérifie si le champ est une colonne présente
                column_query = f"PRAGMA table_info({fk_table});"
                columns = [col[1] for col in self.execute_query(column_query)]

                if "nom" in columns:
                    suggestion_query = f"SELECT id, nom FROM {fk_table}"
                    suggestions[fk_column] = self.execute_query(suggestion_query)
                elif "localisation" in columns:
                    suggestion_query = f"SELECT id, localisation FROM {fk_table}"
                    suggestions[fk_column] = self.execute_query(suggestion_query)
                else:
                    suggestion_query = f"SELECT id FROM {fk_table}"
                    suggestions[fk_column] = self.execute_query(suggestion_query)

            return suggestions

    def get_table_metadata(self, table_name: str) -> dict:
        """
        Récupère les métadonnées d'une table, y compris les clés primaires, colonnes et relations FK.

        :param table_name: Nom de la table cible.
        :return: Dictionnaire contenant les colonnes, clés primaires, et relations FK.
        """
        try:
            # Récupérer les colonnes de la table
            columns_query = f"PRAGMA table_info({table_name})"
            columns = self.execute_query(columns_query)
            column_info = {
                col[1]: {"type": col[2], "notnull": col[3], "pk": col[5]}
                for col in columns
            }

            # Récupérer les clés étrangères
            fk_query = f"PRAGMA foreign_key_list({table_name})"
            foreign_keys = self.execute_query(fk_query)
            relations = [
                {"column": fk[3], "ref_table": fk[2], "ref_column": fk[4]}
                for fk in foreign_keys
            ]

            return {"columns": column_info, "foreign_keys": relations}
        except sqlite3.Error as e:
            print(
                f"Erreur lors de la récupération des métadonnées pour '{table_name}': {e}"
            )
            return {}

    def get_all_tables(self) -> List[str]:
        """Get the list of all tables in the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [table[0] for table in cursor.fetchall()]

    def get_table_as_list(self, table_name: str) -> List[Tuple]:
        """Récupère les données d'une table SQLite et les transforme en tableau."""
        if not self.connection:
            raise ConnectionError(
                "La connexion à la base de données n'est pas établie."
            )

        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return []

    def get_table_columns(self, table_name: str) -> List[str]:
        """Fetches the column names of a SQLite table.

        Args:
            table_name (str): The name of the table.

        Raises:
            ConnectionError: If the connection to the database is not established.

        Returns:
            List[str]: The list of column names.
        """
        if not self.connection:
            raise ConnectionError("The connection to the database is not established.")

        cursor = self.connection.cursor()
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            return [
                {"name": column[1], "type": column[2]} for column in cursor.fetchall()
            ]
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des colonnes: {e}")

    def get_foreign_keys(self, table_name: str) -> List[dict]:
        """Fetch foreign key constraints for a given table.

        Args:
            table_name (str): The name of the table.

        Raises:
            ConnectionError: If the connection to the database is not established.

        Returns:
            List[dict]: A list of dictionaries containing foreign key information.
        """
        cursor = self.connection.cursor()
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        return [
            {"column": fk[3], "ref_table": fk[2], "ref_column": fk[4]}
            for fk in cursor.fetchall()
        ]

    def save_table_from_list(self, table_name: str, data: List[Tuple]):
        """Insère ou met à jour les données dans une table SQLite à partir d'un tableau."""
        if not self.is_admin:
            raise PermissionError(
                "Modification non autorisée : accès réservé aux administrateurs."
            )

        if not self.connection:
            raise ConnectionError(
                "La connexion à la base de données n'est pas établie."
            )

        cursor = self.connection.cursor()
        try:
            # Supprime les anciennes données (optionnel, selon vos besoins)
            cursor.execute(f"DELETE FROM {table_name}")

            # Prépare une commande d'insertion
            placeholders = ", ".join(["?"] * len(data[0]))  # Nombre de colonnes
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

            # Insère les nouvelles données
            cursor.executemany(insert_query, data)
            self.connection.commit()
            print(f"{len(data)} lignes insérées dans la table {table_name}.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion des données: {e}")
