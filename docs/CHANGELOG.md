# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Background Task Handling: Introduced a QThread in PyQt5 for running the PCAP to TS conversion asynchronously, allowing the UI to remain responsive.
- File Selection Dialog: Users can now select multiple .pcap files for conversion via the file dialog.
- Progress Bar: A progress bar has been added to show the conversion status.
- Error Handling UI: Added error messages using QMessageBox to notify users of conversion issues.

### Changed
- UI Layout Refinements: Enhanced the user interface layout for better visibility and improved user experience.
- Button Styling: Updated the design of the buttons for a more modern, clean look.

### Deprecated
- No deprecated features yet.

### Removed
- No features removed.

### Fixed
- Button State Management: Fixed the issue where the "Convert to TS" button remained enabled without files being selected.
- UI Alignment: Fixed minor UI alignment issues with widgets.

### Security
- No security-related changes yet.

---

## [Version 1.1.0] - 2024-11-12

### Added
  **Initial release** of the project with support for:
- PCAP to TS conversion using the tsp tool.
- A basic PyQt5 GUI to select multiple PCAP files and start the conversion.
- A progress bar to show conversion status.

### Changed
-  UI Refinements: Improved the layout and spacing of the interface for better clarity and ease of use.

### Deprecated
- No deprecated features.

### Removed
- None.

### Fixed
- UI Bug Fixes: Fixed minor layout issues, such as button alignment and spacing.

### Security
- No security-related changes yet.

