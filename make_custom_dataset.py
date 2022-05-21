#!/usr/bin/python

import asyncio
from httpx import AsyncClient
import argparse
import itertools
import time


async def download_dataset_async(url: str, currency: str):
    """
    Downloads dataset given URL.
    :param currency: The dataset currency type.
    :param url: The URL holding the dataset.
    :return: The dataset as JSON.
    """
    dataset = []

    async with AsyncClient() as client:
        r = await client.get(url.strip())
        if not r.json()['Data'] or not r.json()['Data']['Data']:
            print(f'The url {url} dataset has wrong structure')
            return dataset

        for item in r.json()['Data']['Data']:
            item['currency'] = currency.strip()
            dataset.append(item)
    return dataset


async def main_async():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    args = parser.parse_args()

    download_tasks = []

    if args.filename:
        with open(args.filename) as f:
            for line in f:
                currency, url = line.strip().split(',')
                download_tasks.append(download_dataset_async(url, currency))

    datasets = await asyncio.gather(*download_tasks)
    join_datasets = list(itertools.chain.from_iterable(datasets))

    with open('custom_dataset.txt', 'w') as f:
        for dataset in join_datasets:
            for key, val in dataset.items():
                f.write(str(val) + '\t')
            f.write('\n')


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main_async())
    end = time.time()
    print(f'Download and make dataset time: {end - start}')


