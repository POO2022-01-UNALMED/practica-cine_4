package gestorAplicacion;

import java.util.ArrayList;

/**
 *
 * @author usuario
 */
public class Pelicula {
    private String nombre;
	private String director;
	private int ano;
	private int duracion;
	private String genero;
	private String pais;
	private String calificacion;
	private int precio;
	//Falta por agregar el precio de la pelicula para poder acceder a la pelicula


    public Pelicula(String nombre, String director, int ano, int duracion, String genero, String pais, String calificacion, int precio) {
        this.nombre = nombre;
        this.director = director;
        this.ano = ano;
        this.duracion = duracion;
        this.genero = genero;
        this.pais = pais;
        this.calificacion = calificacion;
		this.precio = precio;
    }
        
	@Override
   public String toString(){
        String varImpr = "Se ha agregado satisfactoriamente una pelicula" ;
        return varImpr;
   }
   
   
	
    public String getNombre() {
		return nombre;
	}
    public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getDirector() {
		return director;
	}
	public void setDirector(String director) {
		this.director = director;
	}
	public int getAno() {
		return ano;
	}
	public void setAno(int ano) {
		this.ano = ano;
	}
	public int getDuracion() {
		return duracion;
	}
	public void setDuracion(int duracion) {
		this.duracion = duracion;
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String genero) {
		this.genero = genero;
	}
	public String getPais() {
		return pais;
	}
	public void setPais(String pais) {
		this.pais = pais;
	}
	public String getCalificacion() {
		return calificacion;
	}
	public void setCalificacion(String calificacion) {
		this.calificacion = calificacion;
	}
	
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	
	

}
