# Soft Drink Delivery System

## Developer
Jonald Sabordo

## Overview
The Soft Drink Delivery System is a web-based application designed to streamline the process of ordering and delivering soft drinks. 
This system allows customers to browse available products, place orders, and track their deliveries. 
It also provides an interface for managing inventory and processing orders.

## Features
- Product catalog with images and detailed information
- User-friendly ordering system
- Order tracking and confirmation
- Inventory management
- Responsive design for mobile and desktop use

## Technology Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default Django database)
- Additional: Font Awesome for icons

## How It Works
1. Product Listing: Users can view a list of available soft drinks, including images, prices, and descriptions.
2. Order Placement: Customers can select products, specify quantities, and provide delivery information to place an order.
3. Order Confirmation: After placing an order, users receive a confirmation with order details and a unique order ID.
4. Order Management: Administrators can view and manage orders through the Django admin interface.
5. Inventory Tracking: The system automatically updates product stock levels as orders are placed.

## Setup Instructions
1. Clone the repository:
2. Install required dependencies:
3. Set up the database:
4. Create a superuser for admin access:
5. Add sample products:
6. Run the development server:
7. Access the application at `http://localhost:8000`

## File Structure
- `delivery/`: Main application directory
- `models.py`: Database models (Product, Order, etc.)
- `views.py`: View functions/classes for handling requests
- `urls.py`: URL configurations for the app
- `templates/`: HTML templates
- `static/`: CSS, JavaScript, and image files
- `softdrink_delivery/`: Project settings directory
- `manage.py`: Django's command-line utility for administrative tasks

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.

## License
This project is licensed under the MIT License.
