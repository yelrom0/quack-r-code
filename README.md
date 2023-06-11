# Quack'R Code

The idea is to be able to provide a URL and a description, and it will generate an amazing looking QR code for you.

## How Do I use it?

_note: This guide is for Linux/Mac and assumes you have docker and docker-compose installed. If you're running Windows, use WSL._

1. If you haven't already, get an OpenAI API key at [Open AI](https://beta.openai.com/).
2. Next, copy `default.env` to `.env`, as `.env` is what's actually read by the backend.
3. For now this is just a placeholder for another step. I made this line longer than it needed to though as you're probably still reading this.
4. Run `docker-compose up -d` to build the image and start the backend.
5. Open your browser and [click on this link](http://localhost:6562/docs). If this doesn't work, check that no services are already running on port 6562.
6. Put in the details.
7. Enjoy!

## Why did I make it?

- I saw an article, looked interesting, and I use QR codes a lot for work. So I thought this would come in handy.

## What Stack Does It Use?

- For the web framework it uses FASTAPI, a fast, lightweight web framework for Python based on Starlette, Pydantic and Typer, I am also using Hypercorn for ASGI.

## Can I modify it?

- Sure! Feel free to modify it and share it with the world.

## Can I test it without running it myself?

- _sigh_ yes, as long as you don't break anything [Quack'R Code @ Morley's Exact Club](https://qr.morleysexact.club/docs)
Sorry, it's not quite ready yet but I'll have it up soon, I promise!

## Will you update this in the future?

- ¯\\\_(ツ)\_/¯ Possibly if issues arise.

## Who am I?

- I'm Daniel Morley, a Python and React Developer from Melbourne, Australia. I enjoy tinkering with my home server and sometimes write small projects like this (and sometimes some larger).
