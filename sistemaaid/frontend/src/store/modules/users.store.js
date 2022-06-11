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
  getPermisos(state){
    return state.permisos[0].groups[0].permissions_code
  }
};

// Mutations
const mutations = {
  set_user(state, data) {
    state.user = data;
  },
  set_permisos(state, data) {
    state.permisos = data;
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
  },

  async permisos({ commit }, user) {
    try {
      const response = await AutorizacionRepository.obtenerPermisos(user);
      commit("set_permisos", response);
    } catch (e) {
      commit("set_error_message", e);
    }
  },



  cerrarSesion({ commit }) {
    commit("reset");
    jwt.destroyToken();
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};