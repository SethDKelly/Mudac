import Fastify from 'fastify';

const app = Fastify({ logger: true });

app.get('/healthz', async () => ({ status: 'ok' as const }));

const host = process.env.API_HOST ?? '127.0.0.1';
const port = Number(process.env.API_PORT ?? '3001');

try {
  await app.listen({ host, port });
} catch (error) {
  app.log.error(error);
  process.exitCode = 1;
}
