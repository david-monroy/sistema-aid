import conn from "../api-connector";
import jwt from "../../common/jwt.service";

export default {
  async obtenerEstados(){
    let response = await conn.post(`/lugares/estados/`, jwt.getAuthHeaderToken());
    return response;
  },
  async obtenerMunicipios(){
    let response = await conn.post(`/lugares/municipios/`, jwt.getAuthHeaderToken());
    return response;
  },
};
