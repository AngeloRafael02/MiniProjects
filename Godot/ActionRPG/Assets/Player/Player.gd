extends KinematicBody2D

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print("Hello World")


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta: float) -> void:
#	pass
const MAX_SPEED = 100
const ACCELERATION = 100
const FRICTION = 400

var velocity = Vector2.ZERO
func _physics_process(delta: float) -> void:
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	input_vector = input_vector.normalized()
	if input_vector != Vector2.ZERO:
		velocity += input_vector*ACCELERATION*delta
		velocity = velocity.clamped(MAX_SPEED*delta)
	else:
		velocity = velocity.move_toward(Vector2.ZERO,FRICTION*delta)
	print(velocity)
	move_and_collide(velocity)
