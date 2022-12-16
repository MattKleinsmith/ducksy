import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import productDetailsReducer from "./productDetails";
import orderDetailsReducer from "./orderDetails";
import productsReducer from "./products";
import buyerReviewsReducer from "./buyerReviews";
import sessionReducer from "./session";
import uiReducer from "./ui";
import ReviewDetailsReducer from "./reviewDetails";
import productReviewsReducer from "./productReviews";
import ShoppingCartReducer from "./shoppingCart";
import productsBySearchReducer from "./productsBySearch";
import searchQueryReducer from "./searchQuery";

const rootReducer = combineReducers({
    session: sessionReducer,
    ui: uiReducer,
    products: productsReducer,
    productDetails: productDetailsReducer,
    productReviews: productReviewsReducer,
    order_details: orderDetailsReducer,
    buyerReviews: buyerReviewsReducer,
    reviewDetails: ReviewDetailsReducer,
    shoppingCarts: ShoppingCartReducer,
    productsBySearch: productsBySearchReducer,
    searchQuery: searchQueryReducer,
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
