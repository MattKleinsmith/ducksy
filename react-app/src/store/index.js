import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import productDetailsReducer from "./productDetails";
import orderDetailsReducer from "./orderDetails";
import productsReducer from "./products";
import reviewsReducer from "./reviews";
import sessionReducer from "./session";
import uiReducer from "./ui";
import ReviewIdReducer from "./reviewId";
import ShoppingCartReducer from "./shoppingCart";

const rootReducer = combineReducers({
    session: sessionReducer,
    ui: uiReducer,
    products: productsReducer,
    productDetails: productDetailsReducer,
    reviews: reviewsReducer,
    order_details: orderDetailsReducer,
    reviewId: ReviewIdReducer,
    shoppingCarts: ShoppingCartReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require("redux-logger").default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
