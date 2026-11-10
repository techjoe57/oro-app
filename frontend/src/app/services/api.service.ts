/**
 * API SERVICE
 *
 * INSTRUCTIONS:
 * 1. Import HttpClient
 * 2. Create methods to call backend APIs
 * 3. Example methods:
 *    - registerUser()
 *    - loginUser()
 */

 // TODO: import HttpClient

 // TODO: create service class

 // TODO: define base API URL (http://localhost:5000)

 // TODO: create register function

 // TODO: create login function
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  getTest() {
    return this.http.get(`${this.baseUrl}/test`);
  }
}