
# Crypto ETL Project

This project implements an ETL (Extract, Transform, Load) pipeline that extracts cryptocurrency price data from an external source, transforms it, and loads it into a PostgreSQL database.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Docker Setup](#docker-setup)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Project Overview

The **Crypto ETL Project** is designed to automate the process of extracting real-time cryptocurrency price data, transforming it, and loading it into a PostgreSQL database for easy access and analysis.

### Key Features:
- Dockerized PostgreSQL database
- Dockerized ETL pipeline in Python
- Wait-for-it script to ensure the database is ready before ETL execution
- Environment variable configuration for easy setup

## Prerequisites

Before starting the project, make sure you have the following installed:

- **Docker**: Used for containerizing the ETL application and PostgreSQL.
- **Docker Compose**: Used to manage multi-container Docker applications.

You can verify if Docker and Docker Compose are installed by running:

```bash
docker --version
docker-compose --version
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto-etl.git
cd crypto-etl
```

### 2. Set up environment variables

Create a `.env` file in the root of your project directory with the following content:

```bash
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

Replace `your_db_user`, `your_db_password`, and `your_db_name` with your desired PostgreSQL credentials.

### 3. Install dependencies

If you're using Docker, all dependencies are already managed in the `Dockerfile` and `requirements.txt`, so you don’t need to install anything manually.

## Running the Project

### 1. Build and start the containers

To build and run the containers with Docker Compose, execute:

```bash
docker-compose up --build
```

This will:
- Start the PostgreSQL database container
- Start the ETL pipeline container
- The ETL container will wait for the PostgreSQL container to be ready before running the ETL job

### 2. Stop the containers

To stop all the running containers:

```bash
docker-compose down
```

### 3. Check logs

You can view the logs of all containers to monitor the progress:

```bash
docker-compose logs
```

## Docker Setup

The project uses Docker Compose for managing the services. It includes:

- **PostgreSQL**: A PostgreSQL database running in a container for storing cryptocurrency data.
- **ETL**: A Python-based ETL pipeline that extracts data from a public API, transforms it, and loads it into the database.

### `docker-compose.yml` Configuration

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:13
    container_name: crypto-postgres
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - crypto-network

  etl:
    build: .
    container_name: crypto-etl
    depends_on:
      - postgres
    command: ["./wait-for-it.sh", "postgres", "5432", "--", "python", "etl.py"]
    environment:
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_HOST: postgres
      DB_PORT: 5432
      DB_NAME: ${DB_NAME}
    networks:
      - crypto-network

volumes:
  postgres_data:

networks:
  crypto-network:
    driver: bridge
```

## Project Structure

```plaintext
crypto-etl/
│
├── docker-compose.yml     # Docker Compose configuration for containers
├── Dockerfile             # Dockerfile to build the ETL container
├── requirements.txt       # Python dependencies for the ETL pipeline
├── wait-for-it.sh         # Script to wait for PostgreSQL container readiness
├── src/
│   ├── extract.py         # Data extraction logic
│   ├── transform.py       # Data transformation logic
│   ├── load.py            # Data loading logic
│   ├── etl.py             # Orchestrates the ETL process
│   └── main.py            # Entry point for the ETL process
├── .env                   # Environment variables (DB credentials)
└── README.md              # Project documentation
```

## Contributing

We welcome contributions to this project! If you'd like to contribute:

1. Fork the repository
2. Create a new branch
3. Implement your changes
4. Submit a pull request

Please make sure to follow the existing code style and write tests for any new functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀
