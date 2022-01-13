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
  async cargarListaCodigo(archivo) {
    let response = await conn.post(`/categoria/cargar/`, archivo, headers);
    return response.data;
  }

};