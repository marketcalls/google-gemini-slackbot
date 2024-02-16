
# Slack Bot with Google Gemini

This Slack Bot integrates Google Gemini's AI technology into Slack, offering a smart, responsive assistant that enhances productivity. Follow these steps to set up and deploy your bot.

## Accessing the SlackBot from Slack Channel with an App Mention

![Accessing the SlackBot from Slack Channel with an App Mention
](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-38.png?resize=1024%2C463&ssl=1)

## Accessing the SlackBot Using Direct Message

![Accessing the SlackBot Using Direct Message](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-37.png?resize=1024%2C439&ssl=1)



## Resources

For a detailed step-by-step guide on building this digital assistant, visit [Building a Digital Assistant in Slack with Google Gemini: A Step-by-Step Guide](https://www.marketcalls.in/python/building-a-digital-assistant-in-slack-with-google-gemini-a-step-by-step-guide.html).

## Prerequisites

- Google Gemini API Key
- Slack App with OAuth & Permissions configured
- Python environment with necessary libraries

## Setup Instructions

1. **Obtain Google Gemini API Key**: Visit Google AI Studio and generate an API key for the Gemini API.
2. **Generate Slack App**: Create a new app in Slack and configure basic information, including OAuth scopes required for the bot to function.
3. **Setup Event Subscriptions**: Subscribe to bot events in your Slack app settings to listen for and respond to messages.
4. **Install Your App**: Add your app to your workspace with the necessary permissions.
5. **Development Environment**:
   - Use Visual Studio Code or your preferred IDE.
   - Create a Python virtual environment and activate it.
   - Install necessary Python libraries including Flask, Slack SDK, and Google Gemini libraries.
6. **Implement Your Slack Bot**: Use Flask for handling Slack events and Google Gemini for generating responses.
7. **Deploy Your Application**: Choose between local testing with ngrok or deploying to Google Cloud App Engine for production.
8. **Configure Slack Event Subscriptions**: Update your Slack app's event subscriptions with your deployment's request URL.
9. **Access Your Slack Bot**: Test your bot via direct message or by mentioning it in a channel.

## Dependencies

Ensure your project has all the necessary dependencies by installing the required libraries which include Flask, various Google and Slack SDKs, and other utility libraries.<br>

Flask<br>
google-ai-generativelanguage<br>
google-api-core<br>
google-auth<br>
google-generativeai<br>
googleapis-common-protos<br>
gunicorn<br>
requests<br>
slack_sdk<br>
colorama<br>
python-dotenv<br>

To install the required dependencies for this project, follow the steps below:
Run the following command to install the dependencies listed in `requirements.txt`:

<code>pip install -r requirements.txt</code>

## Deployment

Detailed steps for deploying with ngrok for local testing and Google Cloud App Engine for production, including setting environment variables and configuring app.yaml for GCP. (refer the resource section)

## Contributing

Invite contributions by providing guidelines for submitting pull requests to your project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


