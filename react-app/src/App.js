import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Routes } from "react-router-dom";

import Header from "./components/Header/Header";
import Modals from "./components/Modals/Modals";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import { restoreUser } from "./store/session";
import OrderDetails from "./components/OrderDetails/OrderDetails";
import ShopManager from "./components/ShopManager/ShopManager";
import ProductEditor from "./components/ProductEditor/ProductEditor";
import { getProducts } from "./store/products";
import ShoppingCart from "./components/ShoppingCart/ShoppingCart";

export default function App() {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);

  const setCart = (user) => {
    const cart_storage = window.localStorage.getItem('ducksyCarts');
    const carts = cart_storage ? JSON.parse(cart_storage) : {};
    if (!carts["guest"]) {
      carts["guest"] = {};
    }
    if (user) {
      if (!carts[user.id]) {
        carts[user.id] = {};
      }
      // Merge guest cart to log-in user cart
      carts[user.id] = Object.assign(carts[user.id], carts["guest"]);
      //  Clear guest cart
      carts["guest"] = {};
    }
    window.localStorage.setItem('ducksyCarts', JSON.stringify(carts));
  }

  setCart(user);

  useEffect(() => {
    dispatch(restoreUser());
    dispatch(getProducts());
  }, [dispatch]);

  return (
    <>
      <Modals />
      <Header />
      <Routes>
        <Route path="/" element={<ProductGrid />} />
        <Route path="/listing/:productId" element={<ProductDetails />} />
        <Route path='/your/purchases' element={<OrderDetails />} />
        <Route path='/your/shop' element={<ShopManager />} />
        <Route path='/your/shop/listing/:productId' element={<ProductEditor />} />
        <Route path='/cart' element={<ShoppingCart />} />
      </Routes>
    </>
  );
}
