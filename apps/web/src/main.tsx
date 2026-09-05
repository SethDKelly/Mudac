import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router';

import { App } from './app/App.js';
import './styles.css';

const queryClient = new QueryClient();
const router = createBrowserRouter([{ path: '/', element: <App /> }]);
const root = document.getElementById('root');

if (!root) {
  throw new Error('MUDAC root element is missing');
}

createRoot(root).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </StrictMode>,
);
