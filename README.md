# Discord Giveaway Calculator

A simple calculator to determine your odds of winning Discord giveaways with various requirements.

## Features

- Calculate odds for standard giveaways
- Calculate odds for giveaways with special requirements (invites, messages)
- User-friendly web interface
- Command-line interface

## Installation

1. Make sure you have Python 3.6+ installed
2. Clone or download this repository
3. Install required packages:
```
pip install -r dependencies/requirements.txt
```

## Usage

### Web Interface (Recommended)

Run the calculator with the web interface:

```
python giveaway_odds_calculator.py --web-ui
```

Or simply double-click `dependencies/run_giveaway_odds.bat` (Windows)

### Command Line

Calculate odds directly from the command line:

```
python giveaway_odds_calculator.py --accounts 5 --participants 100 --winners 2
```

Optional parameters:
- `--type`: Specify calculation type (standard, invite, message, multiple)

Or run in interactive mode:

```
python giveaway_odds_calculator.py
```

## Project Structure

- `giveaway_odds_calculator.py` - Main Python application
- `index.html` - Web interface
- `dependencies/` - Supporting files
  - `requirements.txt` - Python dependencies
  - `run_giveaway_odds.bat` - Windows launcher

## How It Works

### Calculation Types

1. **Standard Giveaway**: Basic probability calculation
2. **With Invite Requirements**: Assumes 30% of participants meet invite requirements
3. **With Message Requirements**: Assumes 50% of participants meet message requirements
4. **With Multiple Requirements**: Assumes 15% of participants meet all requirements

### Math Behind The Calculations

The calculator uses probability theory to determine your chances:

- For a single account in a standard giveaway:
  ```
  probability = (number of winners) / (total participants)
  ```

- For multiple accounts:
  ```
  probability = 1 - (1 - winners/participants) ^ (number of accounts)
  ```

## Disclaimer

This tool is for educational purposes only. Only use on Discord servers you own or have explicit permission to test. Unauthorized testing may violate Discord's Terms of Service.

## License

MIT 