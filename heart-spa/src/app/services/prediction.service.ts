import { environment } from 'src/environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Data } from '../models/data';
import { Prediction } from '../models/prediction';

@Injectable()
export class PredictionService {
    baseUrl: string = environment.apiUrl;
    options = {
        headers: new HttpHeaders().append('Content-type', 'application/json'),
    }
    constructor( private http: HttpClient) { }

    predict(data: Data) {
        return this.http.post<Prediction>(this.baseUrl + 'predict', data, this.options)
        .pipe(map( res => res))
    }
}