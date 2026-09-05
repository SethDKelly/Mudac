const heartbeat = setInterval(() => {
  // The worker receives durable work only after later groups add owned adapters/handlers.
}, 60_000);

const stop = (): void => {
  clearInterval(heartbeat);
  process.exitCode = 0;
};

process.once('SIGINT', stop);
process.once('SIGTERM', stop);

console.log('MUDAC worker bootstrap ready');
