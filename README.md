# Hive: PLM Class Project

[![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Qt Framework](https://img.shields.io/badge/Qt-PyQt5+-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://www.qt.io/)
[![License](https://img.shields.io/badge/License-MIT-28A745?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00A651?style=for-the-badge)](README.md)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

> **Streamline Your Product Lifecycle. From Supply to Sales.**

A comprehensive Product Lifecycle Management (PLM) platform designed to optimize operational efficiency, reduce costs, and enhance decision-making across your entire product lifecycle. Built with enterprise-grade features and user-centric design, this platform transforms how organizations manage products, suppliers, inventory, and production processes.

## 🎯 Business Value

- **Operational Efficiency**: Centralize all product and supply chain data in one secure platform
- **Cost Optimization**: Real-time cost tracking, margin analysis, and production insights
- **Risk Mitigation**: Supplier monitoring, batch tracking, and supply chain visibility
- **Data-Driven Decisions**: Advanced analytics and reporting capabilities for strategic planning
- **Role-Based Access**: Secure multi-user environment with admin and viewer permissions

## 🚀 Key Features

### Product Management Suite

- **Comprehensive Product Sheets**: Track ID, name, quantity, containers, versions, production dates, descriptions, and ingredients
- **Cost Intelligence**: Monitor production costs, raw material expenses, selling prices, marketing costs, and calculate margins
- **Stock & Inventory**: Real-time stock level monitoring, expiration tracking, warehouse location management, and CSV export capabilities

### Supply Chain Optimization

- **Supplier Intelligence**: Track supplier activities, monitor availability, and manage detailed supplier profiles
- **Demand Planning**: Filter deliveries by date range, supplier name, and ingredient requirements
- **Production Analytics**: Visualize production trends, filter by date range and factory location

### Advanced Analytics

- **Batch History Management**: Complete lot tracking with filtering and export capabilities
- **Supplier Analytics**: Graphical visualization of supplier performance and trends
- **Stock Trend Analysis**: Monitor inventory patterns and make informed stocking decisions

### Enterprise Features

- **Secure Authentication**: Role-based login system with admin and viewer access levels
- **Data Export**: CSV export functionality across all modules for reporting and analysis
- **Pagination & Search**: Handle large datasets efficiently with intuitive navigation
- **Contextual Actions**: Right-click context menus for streamlined workflows

## 📋 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/atinyshrimp/plm-class-project.git
   cd plm-class-project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the application:
   ```bash
   python src/main.py
   ```

## 🎮 Getting Started

### Dashboard Navigation

The main window provides intuitive access to key business areas:

- **Products**: Manage product portfolios, costs, and inventory
- **People**: Maintain supplier and organizational contacts
- **Processes**: Track production workflows and timelines
- **Data**: Access historical batch records and compliance data

### Core Workflows

#### Adding & Managing Data

- Use intuitive forms to input or modify data across all modules
- Required fields are clearly marked to ensure data quality
- Real-time validation provides immediate feedback

#### Exporting Reports

All major sections support CSV export for:

- Integration with business intelligence tools
- Compliance documentation
- Strategic reporting and analysis

#### Monitoring & Analytics

- Filter data by multiple criteria (date range, product, supplier, location)
- Visualize trends with built-in graphical analytics
- Export insights for stakeholder presentations

## 🏗️ Technical Architecture

### Technology Stack

- **Frontend**: PyQt5 (Native desktop UI)
- **Backend**: Python 3.8+
- **Database**: SQLite with optimized queries
- **Styling**: Custom QSS stylesheets for consistent branding

### Project Structure

```
src/
├── main.py                 # Application entry point
├── globals.py              # Global configurations
├── components/             # UI components & tabs
├── database/               # Database layer & queries
├── dialogs/                # User dialogs & windows
├── utils/                  # Utility functions
└── widgets/                # Reusable widget components
```

### Database

- Relational schema for integrity and performance
- Comprehensive query library in `sql_queries.py`
- Automated population scripts for test data

## 🔐 User Management

### Authentication Levels

- **Admin**: Full access to all features and settings
- **Viewer**: Read-only access to data and reports

### Security Features

- Role-based access control (RBAC)
- Secure login mechanism
- Audit trail for compliance requirements

## 📊 Business Use Cases

### Scenario 1: Manufacturing Company

Use PLM to manage multi-product portfolios with complex supply chains, track production costs in real-time, and optimize inventory across multiple warehouses.

### Scenario 2: Supply Chain Optimization

Monitor supplier performance, track ingredient deliveries, identify supply chain bottlenecks, and reduce procurement costs through data-driven insights.

### Scenario 3: Compliance & Traceability

Maintain comprehensive batch history for regulatory compliance, track product versions and ingredients, and generate audit-ready reports.

### Scenario 4: Cost Management

Break down production costs by component, analyze margins across product lines, and identify cost reduction opportunities through detailed analytics.

## 🛠️ Customization & Styling

The application supports extensive customization:

- Modify the stylesheet in `assets/styles/palette_style.qss` for brand alignment
- Apply custom styles using the `apply_stylesheet()` function in `utils/styling.py`
- Extend components with additional business logic as needed

## 📜 License & Attribution

This project is licensed under the MIT License, allowing both commercial and personal use with attribution.

Developed as a semester project for advanced Product Lifecycle Management coursework.

## 📝 Changelog

For detailed information about updates, improvements, and bug fixes, see [CHANGELOG.md](CHANGELOG.md).
