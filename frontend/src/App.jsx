import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { createBrowserRouter, RouterProvider, Outlet } from 'react-router-dom';
import Navigation from './components/Navigation';
import SplashPage from './components/SplashPage'
import * as sessionActions from './store/session';

function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(true);

  // useEffect(() => {
  //   dispatch(sessionActions.restoreUser()).then(() => {
  //     setIsLoaded(true)
  //   });
  // }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && <Outlet />}
    </>
  );
}

const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <SplashPage />
      }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;