import axios from "axios";
const conn = axios.create({
  //baseURL: baseDomain, //|| "http://localhost:3000/shipthisapi/v1",
  baseURL: "http://localhost:8000/api/v1",
  timeout: 100000,
});

conn.interceptors.response.use((response) => response.data);

export default conn;