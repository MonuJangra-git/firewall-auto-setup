# Firewall Access Control Automation

A comprehensive Python-based firewall management system for Linux servers using `firewalld`. This project automates firewall rule configuration, service management, and provides logging functionality for all firewall operations.

## Features

✅ **Admin Privilege Verification** - Checks if the user has root/admin permissions
✅ **Firewall Installation Check** - Verifies if firewalld is installed
✅ **Firewall Service Management** - Start, stop, restart, and check status
✅ **Rule Configuration** - 11 different firewall rules including:
   - Allow HTTP/HTTPS (ports 80, 443)
   - Allow SSH (port 22)
   - Allow MySQL (port 3306)
   - Allow PostgreSQL (port 5432)
   - Allow/Block traffic from specific IP addresses
   - Allow/Block traffic on specific ports
   - IP-based and port-based filtering with protocol support

✅ **Logging System** - All operations logged to `firewall_rules.log`
✅ **Interactive CLI** - User-friendly menu-driven interface
✅ **Error Handling** - Comprehensive exception handling with timeout protection (20s)

## Requirements

- Linux system with `firewalld` installed
- Python 3.6+
- Root/sudo privileges to manage firewall
- `systemctl` command available

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MonuJangra-git/firewall-auto-setup.git
cd firewall-auto-setup
```

2. Ensure firewalld is installed:
```bash
sudo dnf install firewalld  # For Fedora/RHEL/CentOS
# or
sudo apt install firewalld  # For Debian/Ubuntu
```

## Usage

Run the script with sudo privileges:
```bash
sudo python3 firewall_auto_setup_integrate_with_log_monitoring_project.py
```

### Menu Options

**Main Menu:**
1. Set Rules - Configure firewall rules
2. Manage Firewall Service - Control firewalld service
3. Exit - Close the application

**Rules Menu (Option 1):**
- Options 1-4: Pre-defined rules for common services
- Options 5-11: Custom rules for specific IPs and ports

**Service Management (Option 2):**
- Start/Stop/Restart firewalld
- Check current firewall status

## Log File

All operations are logged to `firewall_rules.log` in the same directory. Check this file to review all firewall changes and operations.

## Project Structure

```
firewall-auto-setup/
├── firewall_auto_setup_integrate_with_log_monitoring_project.py
├── firewall_rules.log (generated after first run)
└── README.md
```

## Functions Overview

- `log_file()` - Logs operations to file and console
- `run_cmd()` - Executes system commands safely with error handling
- `admin_check()` - Verifies admin privileges
- `firewall_check()` - Checks if firewalld is installed
- `firewall_deploy()` - Initializes and enables firewalld
- `rules_setter()` - Applies firewall rules
- `firewall_service_manager()` - Manages firewalld service
- `cli_interface()` - Main menu interface
- `rule_menu()` - Rule selection menu
- `service_menu()` - Service management menu

## Security Notes

⚠️ **Important:**
- Always run with sudo/root privileges
- Validate IP addresses before adding rules
- Test rules thoroughly before deploying to production
- Keep backups of critical firewall configurations
- Review `firewall_rules.log` regularly for unauthorized changes

## Future Improvements

- [ ] Input validation for IP addresses and ports
- [ ] Firewall reload after adding permanent rules
- [ ] Configuration file support
- [ ] Unit tests
- [ ] Rollback mechanism for failed rules
- [ ] Logging levels (DEBUG, INFO, ERROR)
- [ ] Rich-rule syntax validation

## Troubleshooting

**Permission Denied:**
```bash
sudo python3 firewall_auto_setup_integrate_with_log_monitoring_project.py
```

**Firewalld Not Running:**
```bash
sudo systemctl start firewalld
```

**Rules Not Taking Effect:**
Note: `--permanent` rules require a reload. Add this to the script:
```bash
sudo firewall-cmd --reload
```

## License

This project is open source and available for educational and personal use.

## Author

**Monu Jangra**
- GitHub: [@MonuJangra-git](https://github.com/MonuJangra-git)

## Changelog

### v1.0 (Current)
- Initial release with 11 firewall rules
- Interactive CLI interface
- Complete logging system
- Admin privilege verification
- Service management functionality
