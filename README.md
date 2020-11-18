# ps5avail

## Docker

### build

`docker build --pull --rm -f "Dockerfile" -t ps5avail:latest "."`

### create telegram-send.conf

create a file with the following content:

```ini
[telegram]
token = 12345678:AJKhsjUJHJjOAZI00HvY51qNevj6J2EBijo
chat_id = 1234567890
```

make sure to replace token and chat_id with your own values.

[get token from botfather - telegram.org](https://core.telegram.org/bots#6-botfather)
[how to get a group chat id? - stackoverflow.com](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)

### run (once)

`docker run --name klopypier -d -v $(pwd)/telegram-send.conf:/root/.config/telegram-send.conf ps5avail:latest`

### run (another run)

`docker start ps5avail`
