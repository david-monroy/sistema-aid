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

};