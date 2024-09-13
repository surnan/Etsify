import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import SplashPage from '../components/SplashPage/SplashPage';
import ProductDetails from '../components/ProductDetails';
import Page404 from '../components/404';
import CreateProduct from '../components/CreateProduct/CreateProduct';


export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <SplashPage />,
      },
      {
        path: '/products/:productId',
        element: <ProductDetails />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: '/products/new',
        element: <CreateProduct />
      },
      {
        path: '/404',
        element: <Page404 />,
      },
      {
        path: "*",
        element: <Page404 />
      }
    ],
  },
]);