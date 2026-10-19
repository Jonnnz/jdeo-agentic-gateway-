import asyncio
import os
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("jdeo-agent-worker")

class JDEOAgentWorker:
    def __init__(self, gateway_url: str, bearer_token: str):
        self.gateway_url = gateway_url
        self.bearer_token = bearer_token
        self.is_running = True

    async def poll_stream(self):
        logger.info("Initializing J.DEO 1.1.1 asynchronous worker stream...")
        while self.is_running:
            try:
                await asyncio.sleep(2.0)
                mock_task = {"task_id": "sol-agent-001", "action": "analyze_bounty_feed"}
                await self.process_task(mock_task)
            except Exception as e:
                logger.error(f"Worker stream exception: {e}")
                await asyncio.sleep(5.0)

    async def process_task(self, task: Dict[str, Any]):
        logger.info(f"Processing task [{task['task_id']}]: {task['action']}")
        await asyncio.sleep(1.0)
        logger.info(f"Task [{task['task_id']}] successfully completed and persisted.")

    async def shutdown(self):
        self.is_running = False
        logger.info("J.DEO worker gracefully shut down.")

if __name__ == "__main__":
    gateway_url = os.getenv("JDEO_GATEWAY_URL", "https://jdeo-gateway-111.internal-mesh.net")
    bearer_token = os.getenv("JDEO_API_BEARER_TOKEN", "mock-secure-token")
    
    worker = JDEOAgentWorker(gateway_url, bearer_token)
    try:
        asyncio.run(worker.poll_stream())
    except KeyboardInterrupt:
        asyncio.run(worker.shutdown())
