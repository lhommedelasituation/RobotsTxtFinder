import asyncio
import requests
import argparse


async def check_robot_async(url, user_agent, timeout):
    try:
        host = requests.utils.urlparse(url).hostname
        robots_url = f'http://{host}/robots.txt'
        async with aiohttp.ClientSession() as session:
            async with session.get(robots_url, headers={'User-Agent': user_agent}, timeout=timeout) as response:
                if response.status == 200:
                    return url
    except:
        pass


def check_robot_sync(url, user_agent, timeout):
    try:
        host = requests.utils.urlparse(url).hostname
        robots_url = f'http://{host}/robots.txt'
        response = requests.get(robots_url, headers={'User-Agent': user_agent}, timeout=timeout)
        if response.status_code == 200:
            return url
    except:
        pass


async def main(urls, user_agent, concurrency, timeout, sync):
    accessible_robot_urls = []
    tasks = []

    if sync:
        check_robot = check_robot_sync
    else:
        check_robot = check_robot_async

    async with asyncio.Semaphore(concurrency):
        for url in urls:
            task = asyncio.ensure_future(check_robot(url, user_agent, timeout))
            tasks.append(task)

        for completed_task in asyncio.as_completed(tasks):
            result = await completed_task
            if result is not None:
                accessible_robot_urls.append(result)

    with open('accessible_robot_urls.txt', 'w') as f:
        for url in accessible_robot_urls:
            f.write(f'{url}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vérifie la disponibilité du fichier "robots.txt" pour un ensemble d\'URLs')
    parser.add_argument('urls_file', help='Chemin vers le fichier contenant les URLs à vérifier (par exemple /chemin/vers/urls.txt)')
    parser.add_argument('--user-agent', '-ua', default='Python requests', help='User agent à utiliser (default: Python requests)')
    parser.add_argument('--concurrency', '-c', type=int, default=10, help='Nombre maximum de requêtes simultanées (default: 10)')
    parser.add_argument('--timeout', '-t', type=int, default=5, help='Temps d\'attente maximum pour chaque requête en secondes (default: 5)')
    parser.add_argument('--sync', action='store_true', help='Utiliser des requêtes synchrones au lieu d\'asynchrone (default: False)')
    args = parser.parse_args()

    user_agent = args.user_agent
    url_list = [line.rstrip('\n') for line in open(args.urls_file)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(url_list, user_agent, args.concurrency, args.timeout, args.sync))
    loop.close()
