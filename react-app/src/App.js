import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { restoreUser } from "./store/session";
import { getProducts } from "./store/products";
import Header from "./components/Header/Header";
import AppRoutes from "./AppRoutes";
import Footer from "./components/Footer/Footer";
import Modals from "./components/Modals/Modals";

export default function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(restoreUser());
    dispatch(getProducts());
  }, [dispatch]);

  return (
    <>
      <Header />
      <AppRoutes />
      <Footer />

      <Modals />
    </>
  );
}
