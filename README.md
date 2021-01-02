# Steam playercount to discord webhook

Simple script to periodically check steam API for playercount for a game and send it to discord using webhooks.

## Usage

### Installation

Assuming you have a recent python 3 and pip installed: 

`pip install -r requirements.txt`

`python main.py`

### Config

Change the `config.example.json` and rename it to `config.json`:

**Fields**
| **Field name**   | **type**              | **description**                                                  |
|------------------|-----------------------|------------------------------------------------------------------|
| webhook_image    | url (jpeg/png)        | The profile image that will appear on the webhook.               |
| webhook_title    | string                | The title for the embed the webhook sends.                       |
| webhook_message  | string                | A message that will appear above the embed (for pinging a role). |
| webhook_username | string                | The username for the webhook.                                    |
| game_id          | int                   | The steam app id for the game.                                   |
| webhook_url      | url (discord webhook) | The webhook url.                                                 |
| threshold        | int                   | The difference in player count for which to send a message.      |

