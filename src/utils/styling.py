# Load and apply the external stylesheet file with dynamic color replacements
def apply_stylesheet(widget, file_name):
    # Define color variables
    primary_color       = "#D18F43"     # Honey Brown
    accent_color        = "#F4C542"     # Gold Yellow
    background_color    = "#FAF3E0"     # Light Cream
    text_color          = "#4A3B2C"     # Dark Brown
    hover_color         = "#F4C542"     # Gold Yellow
    selected_color      = "#16A085"     # Darker Teal

    # Read the QSS file
    with open(file_name, "r") as file:
        stylesheet = file.read()
    
    # Replace placeholders with actual color values
    stylesheet = stylesheet.replace("primary_color", primary_color)
    stylesheet = stylesheet.replace("accent_color", accent_color)
    stylesheet = stylesheet.replace("background_color", background_color)
    stylesheet = stylesheet.replace("text_color", text_color)
    stylesheet = stylesheet.replace("hover_color", hover_color)
    stylesheet = stylesheet.replace("selected_color", selected_color)
    
    # Apply the stylesheet
    widget.setStyleSheet(stylesheet)