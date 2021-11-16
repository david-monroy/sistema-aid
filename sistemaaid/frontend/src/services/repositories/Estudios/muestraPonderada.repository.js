import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
    "Content-Type": 'multipart/form-data',
    Accept: 'multipart/form-data',
    Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async cargarMuestra(archivo) {
    let response = await conn.post(`/muestraPonderada/cargar`, archivo, headers);
    return response.data;
  },

  async insertarMuestra(data) {
    let response = await conn.post(`/muestraPonderada/insertar`, data, headers);
    return response;
  },

};