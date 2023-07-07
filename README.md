[![banner-github.png](https://i.postimg.cc/Zq959qLt/banner-github.png)](https://postimg.cc/GBCCVdNq)
<h1 align="center">SMSpoof</h1>
<p align="center">
   SMSpoof is a robust, Python-based tool designed to leverage the power of the Textbelt API, allowing users to anonymously send customized, scheduled, and mass text messages. Created with red team operations in mind, it offers the capacity to send an SMS to a multitude of targets with a single command. However, its uses are not confined to penetration testing scenarios, it can be employed in a wide array of areas requiring SMS notifications, alerts, or even pranks!
</p>

<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" height="25"> <img src="https://camo.githubusercontent.com/8341cfbe224718e1c2334bc81363673efd2565f8b6878314a96d03e4ce42213b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6369636972656c6c6f2f6d6f6469666965642d6c616d2d6578706572696d656e74733f6c6f676f3d476974487562" height="25">

# 📖 Features
1. Customizable Messages: Customize your text messages to suit your specific requirements.
2. Mass Messaging: SMS multiple numbers simultaneously with a single command using a wordlist.
3. Scheduling: Schedule the sending of your messages at a specific date and time.
4. Textbelt API Integration: Leverages the simple, straightforward Textbelt API.
5. Red Team Operations: A handy tool for red team operations and penetration testing scenarios.

# ⚙️ Installation
Clone the repository and navigate to the project folder:
``` bash
git clone https://github.com/LowLevelEngineer/SMSpoof.git
cd SMSpoof
```
Install the required Python libraries:
``` bash
pip install -r requirements.txt
```
The script is already prepared to be used as an executable. To make it callable from anywhere, perform the following steps:

1. Create a directory named bin in your home folder if it doesn't already exist:
``` bash
mkdir ~/bin
```
2. Move the SMSpoof script to this new directory:
``` bash
mv SMSpoof ~/bin
```
3. Add this directory to your PATH by editing your .bashrc, .bash_profile, or .zshrc file:
``` bash
echo 'export PATH=$PATH:~/bin' >> ~/.bashrc  # or ~/.bash_profile, or ~/.zshrc
```
4. Update your current session:
``` bash
source ~/.bashrc  # or ~/.bash_profile, or ~/.zshrc
```
Now, you can run SMSpoof from any directory by typing SMSpoof.

# ▶️ Usage
Run the command with necessary options. Here's an example:
``` bash
SMSpoof -n 1234567890 -m "Hello, world!" -k my-custom-key
```
And here's an explanation of each option:

- -n, --number: The phone number to which the message should be sent.
- -w, --wordlist: File path to a list of phone numbers, each number should be on a new line.
- -m, --message: The text message to be sent.
- -k, --key: The custom key for authentication with the Textbelt API.
- -d, --delay: Delay in seconds between each message.
- -f, --file: File path to include a text file as the content of the message.
- -s, --schedule: Schedule the message to be sent at a specific date and time (format: 'YYYY-MM-DD HH:MM').
Use -h for help with flags.

# 💻 Examples
Here are some examples of how you can use SMSpoof:

Send a message to a specific number:
``` bash
SMSpoof -n 1234567890 -m "Hello, World!" -k your_api_key
```
Send a message to multiple numbers from a wordlist (mass messaging):
```bash
SMSpoof -w numbers.txt -m "Hello, World!" -k your_api_key
```
Send a message from a text file to a specific number:
```bash
SMSpoof -n 1234567890 -f message.txt -k your_api_key
```
Schedule a message for a future time:
``` bash
SMSspoof -n 1234567890 -m "Hello, Future!" -s "2023-12-31 23:59" -k your_api_key
```

# 💾 Limitations and Considerations
- The timezone used for scheduling is the timezone of the machine running the script.
- The Textbelt API has a limit on the number of messages that can be sent per day. Be mindful of this quota to ensure the effectiveness of your operations.

# 🔑 Obtaining Textbelt Key
To use the Textbelt API, you need to obtain a key. The key is a unique identifier that authorizes you to send messages. Here is how you can get it:

1. Visit Textbelt.
2. Click on "Get API Key".
3. Follow the prompts to sign up and receive your key.
Note: Free users are limited to a certain number of messages per day. Consider purchasing a paid key to increase your limit.

# 📑 Script Architecture
The SMSpoof script is structured as follows:

1. Input Data: Accepts inputs through command-line arguments or prompts the user if required inputs are not provided.
2. Message Scheduling: Utilizes the Python datetime and time libraries to schedule message sending.
3. Textbelt API Integration: Sends an HTTP POST request to the Textbelt API with the phone number, message, and custom key.
4. Status Check: Checks and prints the status of the sent message.
5. Mass Messaging: Loops over a list of phone numbers to send the message to multiple recipients.
6. Delays: Introduces an optional delay between each sent message to prevent triggering rate limits or spam detectors.

# 🧑‍💻 Contributing
Contributions to SMSpoof are welcome! Feel free to open an issue or submit a pull request if you have a feature suggestion or found a bug.

# 📋 License
SMSpoof is released under the MIT License. See the LICENSE file for details.

# ⚖️ Legal Disclaimer:
**FOR EDUCATIONAL PURPOSES ONLY!** <br />
Misuse of **SMSpoof** is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program. Use Responsibly!
<br />
