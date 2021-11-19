from __future__ import annotations
import asyncio

__all__ = ("Task")


class Task:
    """
    Create loop task to run forever
    to start call start(*args, **kwargs)
    """

    def __init__(self, core, *, intervel: int | float) -> None:
        self.core = core
        self.intervel = intervel
        self.loop = asyncio.get_event_loop()
        self._task: asyncio.Task[None] = None
        self._stats: bool = True
        self.result = None

    async def _loop(self, *args, **kwargs):
        while self._stats:
            self.result = await self.core(*args, **kwargs)
            await asyncio.sleep(self.intervel)

    def start(self, *args, **kwargs) -> None:
        """
        To start task
        """
        task = self.loop.create_task(self._loop(*args, **kwargs))
        self._task = task

    def cancel(self) -> None:
        """
        To stop task
        """
        self._stats = False
        self._task.cancel()
