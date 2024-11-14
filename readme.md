# Facebook Group Auto Decline Bot

An automated tool to decline posts in a Facebook group based on specified conditions, 
designed for group administrators who want to manage posts efficiently and reduce unwanted content.

## Features

- **Automated Decline**: Automatically finds and clicks the "Decline" button on posts in the target Facebook group.
- **Error Handling**: Tracks internet connection issues and consecutive errors with retry attempts.
- **Interval Checks**: Periodically refreshes and checks for new posts to decline every 5 minutes.
- **Customizable Settings**: Allows customization of the Firefox profile path and target Facebook group URL.

## Requirements

- **Python 3.8+**
- **Selenium**
- **Mozilla Firefox**

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yunustalhat/fb-group-auto-decline-bot.git
   cd fb-group-auto-decline-bot
   ```

2. **Install Required Packages**:
   Install the necessary Python dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Firefox Profile Path**:
   Open `main.py` and update the `profile_path` variable with the path to your Firefox profile:
   ```python
   profile_path = "/path/to/your/firefox/profile"  # CHANGE THIS
   ```

2. **Set Facebook Group URL**:
   Update the `driver.get` URL in `main.py` with the URL of your target Facebook group:
   ```python
   driver.get("https://www.facebook.com/groups/your-group-id"/spam)  # CHANGE THIS
   ```

## Usage

To run the bot, use the following command in your terminal:
```bash
python main.py
```

The bot will begin declining posts automatically in the specified Facebook group.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Repository Owner

yunustalhat
