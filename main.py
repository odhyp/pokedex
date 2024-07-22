from src.data_fetcher import DataFetcher


def main():
    data_fetcher = DataFetcher()
    sample = data_fetcher.fetch_pokemon_data(1)
    print(sample)


if __name__ == '__main__':
    main()
