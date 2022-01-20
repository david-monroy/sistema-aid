import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
    "Content-Type": 'multipart/form-data',
    Accept: 'multipart/form-data',
    Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async crear(data) {
    let response = await conn.post(`/listaCodigo/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async consultar() {
    let response = await conn.get(`/listaCodigo/`, jwt.getAuthHeaderToken());
    return response;
  },

  async cargarListaCodigo(archivo,idLista) {
    let response = await conn.post(`/categoria/cargar/${idLista}`, archivo, headers);
    return response.data;
  },

  async obtenerCategorias(idLista) {
    let response = await conn.get(`/categoria/consultar/${idLista}`, jwt.getAuthHeaderToken());
    return response;
  },

  async eliminarCategoria(id) {
    let response = await conn.delete(`/categoria/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },

  async editarCategoria(id, data) {
    let response = await conn.put(`/categoria/${id}/`, data, jwt.getAuthHeaderToken());
    return response;
  },

  async crearCategoria(data) {
    let response = await conn.post(`/categoria/`, data, jwt.getAuthHeaderToken());
    return response;
  },

};