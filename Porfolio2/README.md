# Act 02 - Interactive Command Menu

This project implements a command-line interface (CLI) menu in Python that allows users to perform system checks such as disk usage analysis, active user listing, and IP validation for ping simulation.

---

## Features

1. **Disk Usage (`1`)**: Prompts for disk usage percentage and returns status alerts:
   - **CRITICAL**: If usage is over `90%`.
   - **WARNING**: If usage is over `80%`.
   - **OK**: For normal disk usage.
2. **Users (`2`)**: Displays a list of active system users.
3. **Ping (`3`)**: Prompts for an IP address and verifies that it contains exactly 4 octets separated by dots before simulating a ping.
4. **Quit (`q`)**: Exits the application cleanly.

---

## Comparison: `match-case` vs `if-elif-else`

### 1. Readability and Structure
- **`match-case`**: Provides a cleaner, highly readable structure when matching a single variable (`option`) against multiple explicit values. The wildcard pattern (`case _:`) acts as an intuitive fallback for unhandled inputs.
- **`if-elif-else`**: The traditional conditional approach. It requires repeating the condition expression (`option == ...`) for every branch, which can lead to repetitive code.

### 2. Version Compatibility
- **`match-case`**: Requires Python 3.10 or higher (Pattern Matching support).
- **`if-elif-else`**: Compatible with all versions of Python.

### Conclusion
For single-variable selection menus, `match-case` offers a more elegant and idiomatic solution provided Python 3.10+ is available.