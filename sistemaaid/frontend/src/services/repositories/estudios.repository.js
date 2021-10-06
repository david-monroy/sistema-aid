import conn from "../api-connector";
import jwt from "../../common/jwt.service";

export default {
  async agregar(data) {
    console.log(jwt.getAuthHeaderToken())
    console.log (data)
    let response = await conn.post(`/estudios/`, data, jwt.getAuthHeaderToken());
    return response;
  }
};