const SET_SEARCH_QUERY = 'productsBySearch/SET_SEARCH_QUERY';
const CLEAR_SEARCH_QUERY = 'productsBySearch/CLEAR_SEARCH_QUERY';

export const setSearchQuery = (searchQuery) => {
    return { type: SET_SEARCH_QUERY, searchQuery }
};

export const clearSearchQuery = () => {
    return { type: CLEAR_SEARCH_QUERY }
};

export default function searchQueryReducer(state = '', action) {
    switch (action.type) {
        case SET_SEARCH_QUERY:
            return action.searchQuery;
        case CLEAR_SEARCH_QUERY:
            return '';
        default:
            return state;
    }
};
