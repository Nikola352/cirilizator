class DiscordMessage:
    """
    DiscordMessage represents a message from Discord.
    ---
    properties:
      author:
        type: string
        description: The author of the Discord message.
      message:
        type: string
        description: The content of the Discord message.
    """

    def __init__(self, author, message):
        self.author = author
        self.message = message
        