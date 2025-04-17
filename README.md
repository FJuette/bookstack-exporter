<h1 align="center">Welcome to bookstack-exporter 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Export all books from your bookstack instance as local backup

## Requirements

A bookstack user with export rights to all books and a API token.

## Install

```sh
docker pull bookstack-exporter
```

## Usage

```sh
docker run --name bookstack-exporter --rm -v "/$(pwd)/export":/export -e BOOKSTACK_URL=https://localhost:8443 -e BOOKSTACK_TOKEN=<token_id>:<token_secret> -e EXPORT_FORMAT=html bookstack-exporter
```

The `EXPORT_FORMAT` is optional, default is `pdf`. Valid format are `html`, `pdf` and `markdown`.
Mount a local directory to save the exported files outside the container.

## Run locally

1. Clone the repository
2. [Optional] Create a virtual environment
3. Create a .env (copy from example.env) and fill in your bookstack instance URL and token
4. On linux and macOS, run the following command to run the application (pip packages are installed on the first run):

```sh
make run
```

## Author

👤 **Fabian Jütte**

* Github: [@FJuette](https://github.com/FJuette)

## Show your support

Give a ⭐️ if this project helped you!

***
_The initial README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_