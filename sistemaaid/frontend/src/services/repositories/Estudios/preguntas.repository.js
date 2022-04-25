import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
    "Content-Type": 'multipart/form-data',
    Accept: 'multipart/form-data',
    Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async cargar(data, idEdicion) {
    let response = await conn.post(`/preguntas/cargar/${idEdicion}/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async preview(data) {
    let response = await conn.post(`/preguntas/preview/`, data, headers);
    return response.data;
  }

};