import jwt from "../../common/jwt.service";
import Repository from "../../services/repositories/repositoryFactory";
const AutorizacionRepository = Repository.get("Autorizacion");

// Initial State object
const initialState = () => {
  return { user: {}, tracking_info: {}, tracking_status: {}, error: "" };
};

// State object
const state = initialState();

// Getter functions
const getters = {
  getError(state) {
    return state;
  },
  getUser(state) {
    return state.user;
  },
  getUserId(state) {
    return state.user.id;
  },
};

// Mutations
const mutations = {
  set_user(state, data) {
    state.user = data;
  },
  set_error_message(state, error) {
    state.error = error;
  },
  reset(state) {
    const newState = initialState();
    Object.keys(newState).forEach((key) => {
      state[key] = newState[key];
    });
  },
};

// Actions
const actions = {
  async authorize({ commit }, payload) {
    try {
      const response = await AutorizacionRepository.login(payload);
      jwt.saveToken(response.access);
      commit("set_user", payload);
    } catch (e) {
      commit("set_error_message", e);
    }
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};