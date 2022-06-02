package gestorAplicacion;

public class Persona {
    private int cedula;
    private int celular;
    private String nombre;
    private String sexo;
    private int edad;

    

    public Persona(int cedula,int celular, String nombre, String sexo, int edad) {
        this.cedula = cedula;
        this.celular = celular;
        this.nombre = nombre;
        this.sexo = sexo;
        this.edad = edad;
    }

    public int getCedula() {
        return cedula;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public int getCelular() {
        return celular;
    }

    public void setCelular(int celular) {
        this.celular = celular;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    
}
