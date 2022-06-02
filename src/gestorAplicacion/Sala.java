package gestorAplicacion;

import java.util.ArrayList;
import java.util.Scanner;



public class Sala {
    
    private String tipo;
    
    private ArrayList<Silla> sillas;

    private Pelicula pelicula;
    
    private ArrayList<Trabajador> trabajadores;

	private int numero;

	private int basura;
    

    
    

    
    //Creacion del objeto sala, se le pasa un array de sillas, la pelicula, y tipo si es 3D o 2D
    
    public Sala(String tipo, ArrayList<Silla> sillas, Pelicula pelicula,ArrayList<Trabajador> trabajadores, int numero,int basura) {
		this.tipo = tipo;
		this.sillas = sillas;
		this.pelicula = pelicula;
        this.trabajadores = trabajadores;
		this.numero = numero;
		this.basura = basura;

	}






	public String getTipo() {
		return tipo;
	}






	public void setTipo(String tipo) {
		this.tipo = tipo;
	}






	public ArrayList<Silla> getSillas() {
		return sillas;
	}






	public void setSillas(ArrayList<Silla> sillas) {
		this.sillas = sillas;
	}






	public Pelicula getPelicula() {
		return pelicula;
	}






	public void setPelicula(Pelicula pelicula) {
		this.pelicula = pelicula;
	}






	public ArrayList<Trabajador> getTrabajadores() {
		return this.trabajadores;
	}






	public void setTrabajadores(ArrayList<Trabajador> trabajadores) {
		this.trabajadores = trabajadores;
	}






	public int getNumero() {
		return numero;
	}






	public void setNumero(int numero) {
		this.numero = numero;
	}


	
	public int getBasura() {
		return numero;
	}

	public void setBasura(int numero) {
		this.numero = numero;
	}



    
		
	
	}