import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
    "Content-Type": 'multipart/form-data',
    Accept: 'multipart/form-data',
    Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async cargarMuestra(archivo, tamanoMuestral) {
    let response = await conn.post(`/muestraPonderada/cargar/${tamanoMuestral}`, archivo, headers);
    return response.data;
  },

  async insertarMuestra(data, idEdicion) {
    let response = await conn.post(`/muestraPonderada/insertar/${idEdicion}`, data, headers);
    return response;
  },

};