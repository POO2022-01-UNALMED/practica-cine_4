package gestorAplicacion;

public class Trabajador extends Persona {
    private String cargo;
    private boolean administrador;

    public Trabajador(int cedula,int celular,String nombre, String sexo, int edad,String cargo, boolean administrador) {
		super(cedula, celular, nombre, sexo, edad);
        this.cargo = cargo;
        this.administrador = administrador;
    }
    
	public String getCargo() {
		return cargo;
	}
	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public boolean isAdministrador() {
		return administrador;
	}
	public void setAdministrador(boolean administrador) {
		this.administrador = administrador;
	}
	
	

}
