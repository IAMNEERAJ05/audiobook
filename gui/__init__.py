"""
Audiobook Generator GUI Package

This package contains all the graphical user interface components for the Audiobook Generator application.
It provides a modern, professional interface for creating audiobooks from PDF files.

Main Components:
- HomeWindow: Main application window with navigation
- ProcessingWindow: Book processing interface with progress tracking
- LibraryWindow: Audiobook library management
- PlayerWindow: Audio player for listening to audiobooks
- Components: Reusable UI components (buttons, progress bars, status logs)

Architecture:
The GUI follows a modern design pattern with:
- Clean separation of concerns
- Reusable components
- Consistent styling and theming
- Professional user experience

Author: Seeram Neeraj Kumar
Version: 1.0
"""

# Import main windows for easy access
from .home_window import HomeWindow
from .processing_window_new import ProcessingWindow
from .library_window_new import LibraryWindow
from .player_window_new import PlayerWindow
from .api_key_dialog import APIKeyDialog

# Import components
from .components.buttons import ActionButton, ModernButton, IconButton
from .components.progress_bar import ProgressWidget
from .components.status_log import StatusLogWidget, ModernStatusLog

# Version information
__version__ = "1.0.0"
__author__ = "Seeram Neeraj Kumar"
__description__ = "Professional GUI components for Audiobook Generator"

# Export main classes for easy importing
__all__ = [
    # Main Windows
    'HomeWindow',
    'ProcessingWindow', 
    'LibraryWindow',
    'PlayerWindow',
    'APIKeyDialog',
    
    # Components
    'ActionButton',
    'ModernButton', 
    'IconButton',
    'ProgressWidget',
    'StatusLogWidget',
    'ModernStatusLog',
    
    # Package info
    '__version__',
    '__author__',
    '__description__'
]

# Package metadata
PACKAGE_INFO = {
    'name': 'audiobook_gui',
    'version': __version__,
    'author': __author__,
    'description': __description__,
    'main_windows': ['HomeWindow', 'ProcessingWindow', 'LibraryWindow', 'PlayerWindow'],
    'components': ['ActionButton', 'ModernButton', 'IconButton', 'ProgressWidget', 'StatusLogWidget']
}
