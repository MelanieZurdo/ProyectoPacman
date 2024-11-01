import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.prod';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  /**
   * @description Key de la API obtenida del archivo enviroment de desarrollo
   */
  apiKey = environment.apiKey;

  /**
   * @description Url base predefinida para consumir la API
   */
  apiUrl = `https://api.mediastack.com/v1/news?access_key=`;

  constructor(private http: HttpClient) {}

  /**
   * @function getNews
   * @description Funcion con endpoint desde el cual se obtendran las noticias
   * @param category 
   * @returns 
   */ 
  getNews(category: string): Observable<any> {
    return this.http.get(`${this.apiUrl}${this.apiKey}&categories=${category}&languages=es`);
  }
}