import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
    "Content-Type": 'multipart/form-data',
    Accept: 'multipart/form-data',
    Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async preprocesamiento(data) {
    let response = await conn.post(`/ia/preprocesamiento/`, data, headers);
    return response;
  },
  async entrenar(data, idListaCodigo) {
    let response = await conn.post(`/ia/entrenarModelo/${idListaCodigo}/`, data, headers);
    return response;
  },
};