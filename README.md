<h1 align="center">Welcome to bookstack-exporter 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

## About
> Just want to export all your books from your bookstack instance without touching the UI?

bookstack-export is a simple helper tool that can download all books from your bookstack instance in the format you choose (pdf, markdown or html).
In the bookstack UI you can only export one book at a time. This tool uses the bookstack API to export all books in parallel.

## Prerequirements

A bookstack user with export rights to all books and a API token.

## Usage

```sh
docker run --name bookstack-exporter --rm -v "/$(pwd)/export":/export -e BOOKSTACK_URL=https://localhost:8443 -e BOOKSTACK_TOKEN=<token_id>:<token_secret> -e EXPORT_FORMAT=html fjuette/bookstack-exporter:0.0.1
```

The `EXPORT_FORMAT` is optional, default is `pdf`. Valid format are `html`, `pdf` and `markdown`.
Mount a local directory to save the exported files outside the container.

### Example output

```
__main__ - 2025-04-17 10:59:13,606 - DEBUG - Try to download book Router (Firewall, IDS) as html...
__main__ - 2025-04-17 10:59:13,606 - DEBUG - Try to download book PoE 2 as html...
__main__ - 2025-04-17 10:59:15,091 - DEBUG - Book PoE 2 downloaded successfully.
__main__ - 2025-04-17 10:59:15,188 - DEBUG - Book Router (Firewall, IDS) downloaded successfully.
```

## Run locally

1. Clone the repository
2. [Optional] Create a virtual environment
3. Create a .env (copy from _example.env_) and fill in your bookstack instance URL and token
4. On linux and macOS, run the following command to run the application (pip packages are installed on the first run):

```sh
make run
```

## Versioning

Minor version bumps should be backwards compatible. Major bumps are not.

## Author

Written by 👤 **Fabian Jütte** as a personal project to store / backup my bookstack instance locally.

* Github: [@FJuette](https://github.com/FJuette)

## Show your support

Give a ⭐️ if this project helped you!

## License

bookstack-explorter is distributed under the MIT license. See the included [LICENSE.txt](https://github.com/FJuette/bookstack-exporter/blob/main/LICENSE.txt) file for details.

***
_The initial README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_