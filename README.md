# plm-class-project

A comprehensive Product Lifecycle Management (PLM) tool developed as a semester-long project for our PLM course.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/atinyshrimp/plm-class-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd plm-class-project
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    python src/main.py
    ```

## Usage

### Main Window

-   The main window provides access to various tabs for managing different aspects of the product lifecycle.

### Navigation Bar

-   Use the navigation bar to switch between different sections such as Products, People, Processes, and more.

### Data Tabs

-   Each section contains data tabs for viewing and managing related information.
-   For example, the Products section includes tabs for product details, stock, and location.

### Adding & Editing Data

-   Use the provided forms to add or edit data in each section.
-   Ensure all required fields are filled before submitting the form.

### Styling

-   The application uses a custom stylesheet for a consistent look and feel.
-   You can modify the stylesheet in `palette_style.qss` and apply changes using the `apply_stylesheet` function in `styling.py`.

### Database

-   The application connects to a database to store and retrieve data.
-   Database queries are managed in `sql_queries.py`.

### Shortcuts

-   The application includes various shortcuts for quick access to common actions.
-   Refer to the menu for a list of available shortcuts.

## Functionalities

### Product Management

-   **Product Sheets**: View and manage detailed information about each product, including ID, name, quantity, container, version, production date, description, and ingredients.
-   **Cost Details**: Track and manage production costs, raw materials costs, selling prices, marketing costs, total costs, and margins.
-   **Stock & Location**: Monitor stock levels, expiration dates, arrival dates, warehouse locations, and export data to CSV.

### People Management

-   **Supplier Tracking**: Track supplier activities, view supplier details, and manage supplier data.

### Process Management

-   **Production Tracking**: Track production processes, filter data by date range, product ID, and factory location, and export data to CSV.
-   **Supplier Availability**: Monitor supplier availability, filter data by delivery dates, supplier names, and ingredients, and check for upcoming deliveries.

### Data Management

-   **Batch History**: View and manage batch history, filter data by lot ID, product ID, or status, and export batch history to CSV.

### Additional Features

-   **Login System**: Secure login system with different user roles (admin, viewer).
-   **Context Menus**: Right-click context menus for quick actions on data tables.
-   **Pagination**: Pagination controls for navigating through large datasets.
-   **Export to CSV**: Export data from various tabs to CSV files for external use.
-   **Graphical Analytics**: Visualize supplier analytics and stock trends using graphs.

## Changelog

For a detailed list of changes, refer to the `CHANGELOG.md` file.
